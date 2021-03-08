/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [0,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [1,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [2,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [3,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [4,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
/pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:115: operator(): block: [0,0,0], thread: [5,0,0] Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.
THCudaCheck FAIL file=/pytorch/torch/csrc/generic/serialization.cpp line=31 error=710 : device-side assert triggered
Traceback (most recent call last):
  File "main.py", line 28, in teleport
    teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 28, in learn
    self._learn(state_after, action, reward, done, *args)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 52, in _learn
    self.learner.learn(self.values, state_after, action, reward, done)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/learner.py", line 38, in DoubleQlearn
    loss_value_network.backward()
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/tensor.py", line 245, in backward
    torch.autograd.backward(self, gradient, retain_graph, create_graph, inputs=inputs)
  File "/zhome/ea/9/137501/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/autograd/__init__.py", line 145, in backward
    Variable._execution_engine.run_backward(
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

    Name :                      gold_big_doubleQ-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     11
    Height :                    11
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


      189789 function calls (189488 primitive calls) in 13.37 seconds

##    Ordered by: cumulative time
   List reduced from 391 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   13.376   13.376 {built-in method builtins.exec}
                      1    0.000    0.000   13.376   13.376 <string>:1(<module>)
                      1    0.000    0.000   13.376   13.376 main.py:10(teleport)
                      2    0.000    0.000   12.825    6.413 agent.py:14(__init__)
                      2    0.000    0.000   12.825    6.412 network.py:33(__init__)
                      1    0.000    0.000   12.814   12.814 agent.py:93(__init__)
                      6    0.000    0.000   12.772    2.129 module.py:573(to)
                   72/6    0.001    0.000   12.772    2.129 module.py:385(_apply)
                     54    0.000    0.000   12.771    0.236 module.py:667(convert)
                     55   12.769    0.232   12.770    0.232 {method 'to' of 'torch._C._TensorBase' objects}
                      2    0.000    0.000    0.236    0.118 agent.py:26(learn)
                      2    0.000    0.000    0.234    0.117 learner.py:30(DoubleQlearn)
                      2    0.000    0.000    0.205    0.103 tensor.py:195(backward)
                      2    0.000    0.000    0.205    0.103 __init__.py:68(backward)
                      2    0.205    0.102    0.205    0.102 {method 'run_backward' of 'torch._C._EngineBase' objects}
                      1    0.000    0.000    0.180    0.180 agent.py:50(_learn)
                      1    0.013    0.013    0.123    0.123 agent.py:77(interveen)
                      2    0.000    0.000    0.113    0.056 agent.py:45(__call__)
                      1    0.000    0.000    0.077    0.077 game.py:8(__init__)
                      2    0.000    0.000    0.065    0.033 layers.py:192(update)
                   87/9    0.001    0.000    0.061    0.007 module.py:866(_call_impl)
                      7    0.000    0.000    0.060    0.009 network.py:24(forward)
                      7    0.000    0.000    0.060    0.009 container.py:117(forward)
                    100    0.001    0.000    0.060    0.001 layers.py:233(restart)
                      1    0.000    0.000    0.056    0.056 agent.py:101(_learn)
                      6    0.000    0.000    0.053    0.009 network.py:15(__init__)
                    100    0.000    0.000    0.049    0.000 levels.py:8(__init__)
                    100    0.000    0.000    0.049    0.000 level.py:8(__init__)
                    100    0.008    0.000    0.047    0.000 levels.py:11(generate)
                     12    0.000    0.000    0.040    0.003 conv.py:370(__init__)
                     12    0.009    0.001    0.040    0.003 conv.py:66(__init__)
                      1    0.000    0.000    0.040    0.040 agent.py:88(pre_process)
                     27    0.000    0.000    0.038    0.001 init.py:347(kaiming_uniform_)
                     54    0.036    0.001    0.036    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      1    0.032    0.032    0.032    0.032 agent.py:59(modify)
                     12    0.000    0.000    0.031    0.003 conv.py:114(reset_parameters)
                      2    0.019    0.009    0.029    0.015 exploration.py:53(softmaxer)
                      3    0.000    0.000    0.029    0.010 agent.py:54(modify_board)
                      2    0.028    0.014    0.028    0.014 {built-in method nonzero}
                      3    0.028    0.009    0.028    0.009 {built-in method torch._C._nn.one_hot}
                      1    0.000    0.000    0.027    0.027 save.py:15(__exit__)
                      1    0.000    0.000    0.027    0.027 save.py:18(save)
                      3    0.006    0.002    0.023    0.008 save.py:24(saveObject)
                     14    0.000    0.000    0.022    0.002 conv.py:398(forward)
                     14    0.000    0.000    0.022    0.002 conv.py:390(_conv_forward)
                     14    0.022    0.002    0.022    0.002 {built-in method conv2d}
                      1    0.000    0.000    0.021    0.021 optimizer.py:84(wrapper)
                      1    0.000    0.000    0.020    0.020 grad_mode.py:24(decorate_context)
                      1    0.000    0.000    0.020    0.020 adam.py:55(step)
                    100    0.010    0.000    0.020    0.000 levels.py:76(RFS)
                      1    0.001    0.001    0.019    0.019 _functional.py:53(adam)
                     25    0.000    0.000    0.018    0.001 activation.py:713(forward)
                     25    0.000    0.000    0.018    0.001 functional.py:1364(leaky_relu)
                    200    0.009    0.000    0.018    0.000 layers.py:37(reset)
                     25    0.018    0.001    0.018    0.001 {built-in method torch._C._nn.leaky_relu}
                      1    0.000    0.000    0.018    0.018 agent.py:36(__init__)
                     18    0.000    0.000    0.018    0.001 linear.py:93(forward)
                     18    0.000    0.000    0.018    0.001 functional.py:1737(linear)
                     18    0.018    0.001    0.018    0.001 {built-in method torch._C._nn.linear}
                      8    0.017    0.002    0.017    0.002 {method 'sqrt' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.013    0.013 layers.py:147(__init__)
                      4    0.000    0.000    0.013    0.003 layer.py:26(__init__)
                      2    0.010    0.005    0.010    0.005 {built-in method multinomial}
                     15    0.000    0.000    0.010    0.001 linear.py:75(__init__)
                    400    0.001    0.000    0.010    0.000 layer.py:40(restart)
                      4    0.009    0.002    0.009    0.002 {built-in method flatten}
                      4    0.000    0.000    0.009    0.002 save.py:28(path)
                     15    0.000    0.000    0.009    0.001 linear.py:86(reset_parameters)
                    100    0.001    0.000    0.008    0.000 level.py:34(notUsed)
                    7/3    0.004    0.001    0.008    0.003 {built-in method _pickle.dump}
                   8100    0.007    0.000    0.007    0.000 level.py:25(inverse)
                  11786    0.005    0.000    0.007    0.000 layer.py:76(add)
                      4    0.007    0.002    0.007    0.002 {built-in method zeros}
                      8    0.000    0.000    0.006    0.001 genericpath.py:16(exists)
                      8    0.006    0.001    0.006    0.001 {built-in method posix.stat}
                   9600    0.003    0.000    0.005    0.000 levels.py:33(<genexpr>)
                      8    0.003    0.000    0.004    0.001 layer.py:90(update)
                      3    0.004    0.001    0.004    0.001 {built-in method io.open}
                  24888    0.004    0.000    0.004    0.000 layer.py:100(grid)
                      3    0.003    0.001    0.003    0.001 {built-in method posix.mkdir}
                   2500    0.001    0.000    0.003    0.000 random.py:285(choice)
                   1104    0.002    0.000    0.003    0.000 module.py:950(__setattr__)
                      1    0.000    0.000    0.003    0.003 storage.py:52(__reduce__)
                      1    0.000    0.000    0.003    0.003 serialization.py:333(save)
                      1    0.000    0.000    0.003    0.003 serialization.py:377(_legacy_save)
                      1    0.000    0.000    0.003    0.003 game.py:21(step)
                     74    0.001    0.000    0.003    0.000 module.py:250(__init__)
                  29921    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
                      4    0.002    0.001    0.002    0.001 {method 'long' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.002    0.002 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}
                      1    0.000    0.000    0.002    0.002 layers.py:212(step)
                   3022    0.002    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                   7404    0.001    0.000    0.002    0.000 enum.py:646(__hash__)
                   2400    0.002    0.000    0.002    0.000 {method 'intersection_update' of 'set' objects}
                      1    0.001    0.001    0.002    0.002 replaybuffer.py:27(teleporter_save_data)
                     54    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                   2400    0.002    0.000    0.002    0.000 levels.py:86(<listcomp>)
                     27    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                    201    0.001    0.000    0.002    0.000 random.py:315(sample)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9393243: <gold_big_doubleQ_0> in cluster <dcc> Done

Job <gold_big_doubleQ_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 01:58:30 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 01:58:35 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 01:58:35 2021
Terminated at Mon Mar  8 01:59:08 2021
Results reported at Mon Mar  8 01:59:08 2021

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

    CPU time :                                   6.75 sec.
    Max Memory :                                 112 MB
    Average Memory :                             112.00 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               8080.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   37 sec.
    Turnaround time :                            38 sec.

The output (if any) is above this job summary.

