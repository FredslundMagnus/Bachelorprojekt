/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [0,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [1,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [2,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [3,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [4,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
THCudaCheck FAIL file=/pytorch/torch/csrc/generic/serialization.cpp line=31 error=710 : device-side assert triggered
Traceback (most recent call last):
  File "main.py", line 28, in teleport
    teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 28, in learn
    self._learn(state_after, action, reward, done, *args)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 52, in _learn
    self.learner.learn(self.values, state_after, action, reward, done)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/learner.py", line 37, in DoubleQlearn
    loss_value_network = self.criterion(action_value_before, td_target)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/nn/modules/module.py", line 889, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/nn/modules/loss.py", line 528, in forward
    return F.mse_loss(input, target, reduction=self.reduction)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/nn/functional.py", line 2926, in mse_loss
    return torch._C._nn.mse_loss(expanded_input, expanded_target, _Reduction.get_enum(reduction))
RuntimeError: CUDA error: device-side assert triggered

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 29, in teleport
    collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 16, in __exit__
    self.save()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 21, in save
    self.saveObject(element, start, element.__class__.__name__)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 26, in saveObject
    pickle.dump(element, open(Save.path(start, _class) + name, "wb"))
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/storage.py", line 54, in __reduce__
    torch.save(self, b, _use_new_zipfile_serialization=False)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/serialization.py", line 374, in save
    _legacy_save(obj, opened_file, pickle_module, pickle_protocol)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/serialization.py", line 447, in _legacy_save
    serialized_storages[key]._write_file(f, _should_read_directly(f), True)
RuntimeError: cuda runtime error (710) : device-side assert triggered at /pytorch/torch/csrc/generic/serialization.cpp:31


# Parameters

    Name :                      gold_small_doubleQ-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     7
    Height :                    7
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.DoubleQlearn
    Learner2 :                  Learners.DoubleQlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      98100 function calls (97799 primitive calls) in 10.50 seconds

##    Ordered by: cumulative time
   List reduced from 389 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   10.497   10.497 {built-in method builtins.exec}
                      1    0.000    0.000   10.497   10.497 <string>:1(<module>)
                      1    0.000    0.000   10.497   10.497 main.py:10(teleport)
                      2    0.000    0.000    9.925    4.962 agent.py:14(__init__)
                      2    0.000    0.000    9.924    4.962 network.py:33(__init__)
                      1    0.000    0.000    9.919    9.919 agent.py:93(__init__)
                      6    0.000    0.000    9.883    1.647 module.py:573(to)
                   72/6    0.000    0.000    9.883    1.647 module.py:385(_apply)
                     54    0.000    0.000    9.882    0.183 module.py:667(convert)
                     55    9.880    0.180    9.881    0.180 {method 'to' of 'torch._C._TensorBase' objects}
                      2    0.000    0.000    0.271    0.135 agent.py:26(learn)
                      2    0.000    0.000    0.270    0.135 learner.py:30(DoubleQlearn)
                   87/9    0.000    0.000    0.268    0.030 module.py:866(_call_impl)
                      1    0.000    0.000    0.220    0.220 agent.py:50(_learn)
                      2    0.000    0.000    0.218    0.109 loss.py:527(forward)
                      2    0.000    0.000    0.218    0.109 functional.py:2898(mse_loss)
                      2    0.218    0.109    0.218    0.109 {built-in method torch._C._nn.mse_loss}
                      1    0.009    0.009    0.112    0.112 agent.py:77(interveen)
                      2    0.000    0.000    0.104    0.052 agent.py:45(__call__)
                      1    0.000    0.000    0.091    0.091 save.py:15(__exit__)
                      1    0.000    0.000    0.091    0.091 save.py:18(save)
                      3    0.004    0.001    0.090    0.030 save.py:24(saveObject)
                    7/3    0.001    0.000    0.065    0.022 {built-in method _pickle.dump}
                      1    0.000    0.000    0.065    0.065 storage.py:52(__reduce__)
                      1    0.000    0.000    0.065    0.065 serialization.py:333(save)
                      1    0.000    0.000    0.065    0.065 serialization.py:377(_legacy_save)
                      1    0.064    0.064    0.064    0.064 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}
                      1    0.000    0.000    0.051    0.051 agent.py:101(_learn)
                      7    0.000    0.000    0.050    0.007 network.py:24(forward)
                      7    0.000    0.000    0.050    0.007 container.py:117(forward)
                      6    0.000    0.000    0.042    0.007 network.py:15(__init__)
                     12    0.000    0.000    0.038    0.003 conv.py:370(__init__)
                     12    0.009    0.001    0.038    0.003 conv.py:66(__init__)
                      1    0.000    0.000    0.033    0.033 agent.py:88(pre_process)
                      2    0.021    0.011    0.031    0.016 exploration.py:53(softmaxer)
                      1    0.000    0.000    0.031    0.031 game.py:8(__init__)
                      1    0.000    0.000    0.030    0.030 tensor.py:195(backward)
                      1    0.000    0.000    0.030    0.030 __init__.py:68(backward)
                      1    0.029    0.029    0.029    0.029 agent.py:59(modify)
                      1    0.029    0.029    0.029    0.029 {method 'run_backward' of 'torch._C._EngineBase' objects}
                     27    0.000    0.000    0.028    0.001 init.py:347(kaiming_uniform_)
                     12    0.000    0.000    0.027    0.002 conv.py:114(reset_parameters)
                      2    0.000    0.000    0.027    0.014 layers.py:192(update)
                      3    0.000    0.000    0.026    0.009 agent.py:54(modify_board)
                     54    0.026    0.000    0.026    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      3    0.026    0.009    0.026    0.009 {built-in method torch._C._nn.one_hot}
                    100    0.000    0.000    0.024    0.000 layers.py:233(restart)
                      1    0.000    0.000    0.020    0.020 optimizer.py:84(wrapper)
                      1    0.000    0.000    0.019    0.019 grad_mode.py:24(decorate_context)
                      1    0.000    0.000    0.019    0.019 adam.py:55(step)
                      2    0.019    0.010    0.019    0.010 {built-in method nonzero}
                    100    0.000    0.000    0.019    0.000 levels.py:8(__init__)
                      1    0.000    0.000    0.019    0.019 _functional.py:53(adam)
                    100    0.000    0.000    0.019    0.000 level.py:8(__init__)
                    100    0.003    0.000    0.017    0.000 levels.py:11(generate)
                      8    0.017    0.002    0.017    0.002 {method 'sqrt' of 'torch._C._TensorBase' objects}
                     25    0.000    0.000    0.017    0.001 activation.py:713(forward)
                     14    0.000    0.000    0.017    0.001 conv.py:398(forward)
                     25    0.000    0.000    0.017    0.001 functional.py:1364(leaky_relu)
                     25    0.017    0.001    0.017    0.001 {built-in method torch._C._nn.leaky_relu}
                     14    0.000    0.000    0.017    0.001 conv.py:390(_conv_forward)
                     14    0.017    0.001    0.017    0.001 {built-in method conv2d}
                     18    0.000    0.000    0.015    0.001 linear.py:93(forward)
                     18    0.000    0.000    0.015    0.001 functional.py:1737(linear)
                     18    0.015    0.001    0.015    0.001 {built-in method torch._C._nn.linear}
                      4    0.000    0.000    0.012    0.003 save.py:28(path)
                      4    0.011    0.003    0.011    0.003 {built-in method flatten}
                      2    0.010    0.005    0.010    0.005 {built-in method multinomial}
                      3    0.009    0.003    0.009    0.003 {built-in method io.open}
                      3    0.008    0.003    0.008    0.003 {built-in method posix.mkdir}
                    100    0.003    0.000    0.007    0.000 levels.py:76(RFS)
                    200    0.003    0.000    0.007    0.000 layers.py:37(reset)
                      1    0.000    0.000    0.006    0.006 agent.py:36(__init__)
                      8    0.000    0.000    0.005    0.001 genericpath.py:16(exists)
                      8    0.005    0.001    0.005    0.001 {built-in method posix.stat}
                    400    0.001    0.000    0.005    0.000 layer.py:40(restart)
                      1    0.000    0.000    0.004    0.004 layers.py:147(__init__)
                      4    0.000    0.000    0.004    0.001 layer.py:26(__init__)
                   6158    0.002    0.000    0.003    0.000 layer.py:76(add)
                      4    0.002    0.001    0.002    0.001 {method 'long' of 'torch._C._TensorBase' objects}
                    100    0.000    0.000    0.002    0.000 level.py:34(notUsed)
                      8    0.002    0.000    0.002    0.000 layer.py:90(update)
                     15    0.000    0.000    0.002    0.000 linear.py:75(__init__)
                   1104    0.001    0.000    0.002    0.000 module.py:950(__setattr__)
                     74    0.000    0.000    0.002    0.000 module.py:250(__init__)
                     54    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                   3200    0.001    0.000    0.002    0.000 levels.py:33(<genexpr>)
                     27    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                      1    0.000    0.000    0.002    0.002 game.py:21(step)
                   2500    0.001    0.000    0.001    0.000 level.py:25(inverse)
                  10200    0.001    0.000    0.001    0.000 layer.py:100(grid)
                      1    0.000    0.000    0.001    0.001 layers.py:212(step)
                   5004    0.001    0.000    0.001    0.000 enum.py:646(__hash__)
                    4/1    0.000    0.000    0.001    0.001 __init__.py:144(_lazy_init)
                      1    0.000    0.000    0.001    0.001 replaybuffer.py:8(__init__)
                      1    0.001    0.001    0.001    0.001 replaybuffer.py:11(<listcomp>)
                    201    0.001    0.000    0.001    0.000 random.py:315(sample)
                     15    0.000    0.000    0.001    0.000 linear.py:86(reset_parameters)
                      1    0.001    0.001    0.001    0.001 {built-in method torch._C._cuda_init}
                    900    0.000    0.000    0.001    0.000 random.py:285(choice)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9393241: <gold_small_doubleQ_0> in cluster <dcc> Done

Job <gold_small_doubleQ_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 01:58:30 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 01:58:39 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 01:58:39 2021
Terminated at Mon Mar  8 02:01:07 2021
Results reported at Mon Mar  8 02:01:07 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   4.74 sec.
    Max Memory :                                 262 MB
    Average Memory :                             262.00 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               7930.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   36 sec.
    Turnaround time :                            157 sec.

The output (if any) is above this job summary.

