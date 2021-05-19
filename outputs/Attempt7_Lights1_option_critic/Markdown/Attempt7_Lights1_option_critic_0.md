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
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/optionCritic.py", line 263, in option_critic_run
    option_critic_prime = deepcopy(option_critic)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 16, in __exit__
    self.save()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 21, in save
    self.saveObject(element, start, element.__class__.__name__)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 26, in saveObject
    pickle.dump(element, open(Save.path(start, _class) + name, "wb"))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 34, in path
    os.mkdir("/".join(path))
FileExistsError: [Errno 17] File exists: 'outputs/Attempt7_Lights1_option_critic/Game'


# Parameters

    Name :                      Attempt7_Lights1_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     32
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      36445992864 function calls (35300915107 primitive calls) in 258901.17 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.173 258901.173 {built-in method builtins.exec}
                      1    0.385    0.385 258901.173 258901.173 <string>:1(<module>)
                      1 4360.042 4360.042 258900.788 258900.788 optionCritic.py:195(option_critic_run)
        1515570447/374665197 10821.702    0.000 117481.254    0.000 module.py:866(_call_impl)
               41079008 9716.318    0.000 116340.614    0.003 optionCritic.py:143(actor_loss_fn)
              126767250  816.807    0.000 107540.627    0.001 optionCritic.py:70(get_state)
              126767250 2974.263    0.000 104223.963    0.001 container.py:117(forward)
                1283719   10.010    0.000 71641.071    0.056 tensor.py:195(backward)
                1283719   11.617    0.000 71630.801    0.056 __init__.py:68(backward)
                1283719 71586.346    0.056 71586.346    0.056 {method 'run_backward' of 'torch._C._EngineBase' objects}
              253534500  964.510    0.000 63585.721    0.000 conv.py:398(forward)
              253534500  409.643    0.000 62268.390    0.000 conv.py:390(_conv_forward)
              253534500 61858.746    0.000 61858.746    0.000 {built-in method conv2d}
               41079008 4346.306    0.000 25457.187    0.001 optionCritic.py:91(get_action)
              501432447 1711.582    0.000 23118.335    0.000 linear.py:93(forward)
              501432447  612.126    0.000 20755.325    0.000 functional.py:1737(linear)
              501432447 20017.347    0.000 20017.347    0.000 {built-in method torch._C._nn.linear}
               41079008 1312.699    0.000 13869.206    0.000 optionCritic.py:80(predict_option_termination)
               82158016 1162.889    0.000 9188.797    0.000 distribution.py:34(__init__)
              380301750  531.834    0.000 8685.151    0.000 activation.py:713(forward)
               41079008  653.880    0.000 8294.691    0.000 categorical.py:115(log_prob)
              380301750  474.653    0.000 8153.317    0.000 functional.py:1364(leaky_relu)
              380301750 7578.877    0.000 7578.877    0.000 {built-in method torch._C._nn.leaky_relu}
               41079008  965.990    0.000 7469.426    0.000 categorical.py:49(__init__)
              124339994  488.006    0.000 6888.830    0.000 optionCritic.py:77(get_Q)
               82478945  483.668    0.000 5615.896    0.000 optionCritic.py:88(get_terminations)
                 320929   73.805    0.000 5516.893    0.017 optionCritic.py:116(critic_loss_fn)
               41079008  281.881    0.000 4847.125    0.000 bernoulli.py:34(__init__)
               41079008 3072.937    0.000 4656.635    0.000 constraints.py:398(check)
                1283719   27.159    0.000 3629.283    0.003 optimizer.py:84(wrapper)
                1283719   12.295    0.000 3521.495    0.003 grad_mode.py:24(decorate_context)
                1283719   87.261    0.000 3482.829    0.003 rmsprop.py:56(step)
               41079008  508.572    0.000 3476.504    0.000 distribution.py:240(_validate_sample)
                1283719  132.113    0.000 3295.264    0.003 _functional.py:203(rmsprop)
                1283719    8.302    0.000 3089.883    0.002 game.py:42(step)
                1283719   13.332    0.000 2985.631    0.002 layers.py:827(step)
              126767250  188.392    0.000 2501.918    0.000 activation.py:101(forward)
               41079008 1218.429    0.000 2477.062    0.000 categorical.py:123(entropy)
               41079008 2349.250    0.000 2349.250    0.000 constraints.py:249(check)
              126767250  161.644    0.000 2313.526    0.000 functional.py:1195(relu)
               41079008 2208.616    0.000 2208.616    0.000 constraints.py:364(check)
              126767250 2120.241    0.000 2120.241    0.000 {built-in method relu}
              123237024  229.087    0.000 2050.739    0.000 utils.py:106(__get__)
              287553056 1996.983    0.000 1996.983    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1529691356 1974.944    0.000 1974.944    0.000 {built-in method torch._C._get_tracing_state}
              123878882  198.707    0.000 1843.447    0.000 tensor.py:525(__rsub__)
               41079008  317.639    0.000 1821.102    0.000 bernoulli.py:86(sample)
               17972060 1772.620    0.000 1772.620    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              123237024 1760.917    0.000 1760.917    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1283719   63.986    0.000 1727.613    0.001 layers.py:17(step)
              126767250  122.122    0.000 1715.745    0.000 flatten.py:39(forward)
             1966924048 1696.505    0.000 1696.629    0.000 module.py:934(__getattr__)
               41079008  116.594    0.000 1658.464    0.000 layer.py:106(move)
               41079008   78.819    0.000 1641.692    0.000 categorical.py:88(logits)
              123878882 1609.364    0.000 1609.364    0.000 {built-in method rsub}
              126767250 1593.623    0.000 1593.623    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               41079008  408.665    0.000 1587.457    0.000 categorical.py:108(sample)
              123557953 1587.178    0.000 1587.178    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               41079008   97.497    0.000 1562.873    0.000 utils.py:82(probs_to_logits)
               27398017  655.670    0.000 1391.047    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               82158016  423.545    0.000 1360.414    0.000 functional.py:46(broadcast_tensors)
               82478945 1318.691    0.000 1318.691    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1283720  136.796    0.000 1238.551    0.001 layers.py:793(update)
              123237024 1203.561    0.000 1203.561    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6592456966 1106.630    0.000 1117.735    0.000 {built-in method builtins.len}
               41079008  229.022    0.000 1100.246    0.000 layers.py:844(check)
               14120909   39.285    0.000 1034.635    0.000 tensor.py:575(__iter__)
               14120909  964.894    0.000  964.894    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               41079008  149.465    0.000  953.497    0.000 utils.py:77(clamp_probs)
             6189049038  937.571    0.000  937.571    0.000 {method 'values' of 'collections.OrderedDict' objects}
               41079008  921.015    0.000  921.015    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               41079008  173.250    0.000  920.631    0.000 utils.py:11(broadcast_all)
               41079008  804.032    0.000  804.032    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               82158016  800.371    0.000  800.371    0.000 {built-in method broadcast_tensors}
              124199811  794.757    0.000  794.757    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1283719   80.820    0.000  773.545    0.001 replaybuffer.py:34(save_option_critic)
               41079008  753.141    0.000  753.141    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               27398017   45.512    0.000  735.378    0.000 <__array_function__ internals>:2(prod)
              247115906  710.063    0.000  710.063    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               41079008  685.798    0.000  685.798    0.000 {built-in method clamp}
               27398017   41.864    0.000  680.768    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               82158016  664.430    0.000  664.430    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               27398017   70.160    0.000  638.904    0.000 fromnumeric.py:2912(prod)
               41540120  626.176    0.000  626.176    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 320929  448.101    0.001  583.534    0.002 replaybuffer.py:42(sample_option_critic)
               41079008  582.832    0.000  582.832    0.000 {built-in method bernoulli}
               27398017  147.152    0.000  568.744    0.000 fromnumeric.py:70(_wrapreduction)
               41079008  531.999    0.000  531.999    0.000 {built-in method all}
               41079008  511.879    0.000  511.879    0.000 {built-in method log}
               41079008  504.928    0.000  504.928    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               17972060  480.470    0.000  480.470    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1283719   77.872    0.000  412.496    0.000 optimizer.py:189(zero_grad)
               41079008  378.898    0.000  378.898    0.000 {built-in method multinomial}
               10269760  224.918    0.000  371.046    0.000 layer.py:175(NoRock_update)
                 461145    8.416    0.000  353.478    0.001 layers.py:849(restart)
               27398017  352.241    0.000  352.241    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               41079008   88.888    0.000  349.606    0.000 layers.py:838(isFree)
              123700733  341.329    0.000  341.329    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              126767264  336.228    0.000  336.228    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               41079008  335.645    0.000  335.645    0.000 {method 'expand' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632731: <Attempt7_Lights1_option_critic_0> in cluster <dcc> Exited

Job <Attempt7_Lights1_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:10 2021
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:16:53 2021
Terminated at Wed May 19 23:12:23 2021
Results reported at Wed May 19 23:12:23 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258263.30 sec.
    Max Memory :                                 948 MB
    Average Memory :                             933.74 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15436.00 MB
    Max Swap :                                   -
    Max Processes :                              8
    Max Threads :                                9
    Run time :                                   258995 sec.
    Turnaround time :                            637273 sec.

The output (if any) is above this job summary.

