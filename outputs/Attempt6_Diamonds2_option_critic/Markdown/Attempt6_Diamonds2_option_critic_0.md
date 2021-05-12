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
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/optionCritic.py", line 264, in option_critic_run
    option_critic_prime = deepcopy(option_critic)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 16, in __exit__
    self.save()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 21, in save
    self.saveObject(element, start, element.__class__.__name__)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 26, in saveObject
    pickle.dump(element, open(Save.path(start, _class) + name, "wb"))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 34, in path
    os.mkdir("/".join(path))
FileExistsError: [Errno 17] File exists: 'outputs/Attempt6_Diamonds2_option_critic/Game'


# Parameters

    Name :                      Attempt6_Diamonds2_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal5
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


      21662825218 function calls (20957595891 primitive calls) in 258900.96 seconds

##    Ordered by: cumulative time
   List reduced from 427 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.964 258900.964 {built-in method builtins.exec}
                      1    0.320    0.320 258900.964 258900.964 <string>:1(<module>)
                      1 2529.597 2529.597 258900.644 258900.644 optionCritic.py:195(option_critic_run)
                 790615    5.757    0.000 177815.802    0.225 tensor.py:195(backward)
                 790615    7.242    0.000 177809.938    0.225 __init__.py:68(backward)
                 790615 177786.649    0.225 177786.649    0.225 {method 'run_backward' of 'torch._C._EngineBase' objects}
        933261454/230602384 4522.759    0.000 51208.574    0.000 module.py:866(_call_impl)
               25299680 3798.273    0.000 50600.100    0.002 optionCritic.py:143(actor_loss_fn)
               78073230  375.125    0.000 47861.785    0.001 optionCritic.py:70(get_state)
               78073230 1001.300    0.000 46332.713    0.001 container.py:117(forward)
              156146460  407.197    0.000 29257.151    0.000 conv.py:398(forward)
              156146460  231.701    0.000 28675.677    0.000 conv.py:390(_conv_forward)
              156146460 28443.976    0.000 28443.976    0.000 {built-in method conv2d}
              308675614  712.059    0.000 10160.391    0.000 linear.py:93(forward)
              308675614  289.945    0.000 9142.200    0.000 functional.py:1737(linear)
              308675614 8785.548    0.000 8785.548    0.000 {built-in method torch._C._nn.linear}
               25299680 1466.687    0.000 8700.650    0.000 optionCritic.py:91(get_action)
               25299680  557.872    0.000 6370.746    0.000 optionCritic.py:80(predict_option_termination)
               50599360  568.559    0.000 3477.023    0.000 distribution.py:34(__init__)
                 790615   16.324    0.000 3420.675    0.004 optimizer.py:84(wrapper)
                 790615    9.488    0.000 3358.237    0.004 grad_mode.py:24(decorate_context)
                 790615   46.272    0.000 3331.797    0.004 adam.py:55(step)
                 790615  274.810    0.000 3233.835    0.004 _functional.py:53(adam)
              234219690  231.770    0.000 3104.803    0.000 activation.py:713(forward)
               25299680  248.331    0.000 2897.921    0.000 categorical.py:115(log_prob)
              234219690  235.253    0.000 2873.033    0.000 functional.py:1364(leaky_relu)
              234219690 2586.903    0.000 2586.903    0.000 {built-in method torch._C._nn.leaky_relu}
               25299680  198.000    0.000 2505.999    0.000 bernoulli.py:34(__init__)
               76432461  174.696    0.000 2470.352    0.000 optionCritic.py:77(get_Q)
               25299680  329.790    0.000 2435.250    0.000 categorical.py:49(__init__)
                 197653   32.290    0.000 2174.850    0.011 optionCritic.py:116(critic_loss_fn)
               50797013  192.048    0.000 1955.147    0.000 optionCritic.py:88(get_terminations)
               25299680  994.323    0.000 1478.007    0.000 constraints.py:398(check)
                 790615    3.903    0.000 1400.153    0.002 game.py:42(step)
                 790615    7.224    0.000 1353.946    0.002 layers.py:827(step)
               25299680  205.660    0.000 1169.010    0.000 distribution.py:240(_validate_sample)
               25299680  203.977    0.000  967.772    0.000 bernoulli.py:86(sample)
               25299680  922.824    0.000  922.824    0.000 constraints.py:364(check)
               78073230   96.969    0.000  912.727    0.000 activation.py:101(forward)
                 790615   34.049    0.000  834.900    0.001 layers.py:17(step)
             1210948743  825.666    0.000  825.724    0.000 module.py:934(__getattr__)
               78073230   95.420    0.000  815.758    0.000 functional.py:1195(relu)
               25299680  418.230    0.000  802.907    0.000 categorical.py:123(entropy)
               25299680   60.829    0.000  797.722    0.000 layer.py:106(move)
               25299680  755.539    0.000  755.539    0.000 constraints.py:249(check)
              177097760  745.688    0.000  745.688    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               75899040  101.107    0.000  723.199    0.000 utils.py:106(__get__)
               78073230   75.742    0.000  718.233    0.000 flatten.py:39(forward)
               78073230  707.209    0.000  707.209    0.000 {built-in method relu}
               76294346   86.210    0.000  701.912    0.000 tensor.py:525(__rsub__)
               22137208  691.568    0.000  691.568    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               50599360  238.111    0.000  662.603    0.000 functional.py:46(broadcast_tensors)
               78073230  642.491    0.000  642.491    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               76294346  602.174    0.000  602.174    0.000 {built-in method rsub}
               25299680  165.329    0.000  577.807    0.000 categorical.py:108(sample)
               25299680  124.520    0.000  572.282    0.000 utils.py:11(broadcast_all)
               11068604  563.155    0.000  563.155    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               50797013  559.788    0.000  559.788    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               11068604  557.360    0.000  557.360    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8696765   19.979    0.000  552.681    0.000 tensor.py:575(__iter__)
               25299680   28.205    0.000  547.111    0.000 categorical.py:88(logits)
               76096693  539.805    0.000  539.805    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              941958219  539.071    0.000  539.071    0.000 {built-in method torch._C._get_tracing_state}
                8696765  520.445    0.000  520.445    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             4032341234  513.906    0.000  519.469    0.000 {built-in method builtins.len}
               25299680   31.996    0.000  518.906    0.000 utils.py:82(probs_to_logits)
                 790616   68.421    0.000  508.414    0.001 layers.py:793(update)
               75899040  501.071    0.000  501.071    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               25299680  105.781    0.000  480.501    0.000 layers.py:844(check)
               75899040  437.811    0.000  437.811    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             3811119046  426.363    0.000  426.363    0.000 {method 'values' of 'collections.OrderedDict' objects}
               11068604  394.595    0.000  394.595    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 197653  309.674    0.002  382.367    0.002 replaybuffer.py:42(sample_option_critic)
               25299680  375.881    0.000  375.881    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               22137208  375.735    0.000  375.735    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11068604  372.439    0.000  372.439    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               50599360  357.452    0.000  357.452    0.000 {built-in method broadcast_tensors}
                 790615   36.302    0.000  306.244    0.000 replaybuffer.py:34(save_option_critic)
               25299680   62.694    0.000  304.371    0.000 utils.py:77(clamp_probs)
               25299680  286.988    0.000  286.988    0.000 {built-in method bernoulli}
               76491999  279.786    0.000  279.786    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               25299680  246.051    0.000  246.051    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               25299680  241.677    0.000  241.677    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               25437795  238.453    0.000  238.453    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              152193386  230.250    0.000  230.250    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               50599360  210.253    0.000  210.253    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                 790615   36.403    0.000  210.021    0.000 optimizer.py:189(zero_grad)
               25299680  206.210    0.000  206.210    0.000 {built-in method clamp}
               25299680   44.417    0.000  202.907    0.000 layers.py:838(isFree)
               76038766  187.608    0.000  187.608    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               25299680  182.539    0.000  182.539    0.000 {built-in method log}
               25299680  177.838    0.000  177.838    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              332972551  115.342    0.000  176.532    0.000 {built-in method builtins.isinstance}
                5534312  101.651    0.000  172.429    0.000 layer.py:175(NoRock_update)
               78073244  166.498    0.000  166.498    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               25299680  162.565    0.000  162.565    0.000 {built-in method all}
              147295688  134.346    0.000  158.489    0.000 layer.py:103(isFree)
               25299680  148.562    0.000  148.562    0.000 {built-in method multinomial}
               75899072   51.446    0.000  146.118    0.000 {built-in method builtins.all}
               26090321   74.830    0.000  142.290    0.000 grad_mode.py:119(__enter__)


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
Subject: Job 9624150: <Attempt6_Diamonds2_option_critic_0> in cluster <dcc> Exited

Job <Attempt6_Diamonds2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:26 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:27 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

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

    CPU time :                                   258228.88 sec.
    Max Memory :                                 1016 MB
    Average Memory :                             1003.16 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15368.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

