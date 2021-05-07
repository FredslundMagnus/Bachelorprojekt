
# Parameters

    Name :                      Attempt2_SuperLevel1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     25
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      49185334483 function calls (47586005175 primitive calls) in 258893.46 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.625 258900.625 {built-in method builtins.exec}
                      1    0.341    0.341 258900.625 258900.625 <string>:1(<module>)
                      1 6039.450 6039.450 258900.284 258900.284 optionCritic.py:195(option_critic_run)
               56875125 10135.366    0.000 117879.790    0.002 optionCritic.py:143(actor_loss_fn)
        2112161410/520226659 10680.650    0.000 115557.270    0.000 module.py:866(_call_impl)
              176881639  888.205    0.000 107828.702    0.001 optionCritic.py:70(get_state)
              176881639 2370.194    0.000 104269.425    0.001 container.py:117(forward)
                2275005   17.137    0.000 69074.689    0.030 tensor.py:195(backward)
                2275005   22.037    0.000 69057.246    0.030 __init__.py:68(backward)
                2275005 68983.618    0.030 68983.618    0.030 {method 'run_backward' of 'torch._C._EngineBase' objects}
              353763278 1005.016    0.000 65299.008    0.000 conv.py:398(forward)
              353763278  569.886    0.000 63835.130    0.000 conv.py:390(_conv_forward)
              353763278 63265.244    0.000 63265.244    0.000 {built-in method conv2d}
              697108298 1708.984    0.000 22354.262    0.000 linear.py:93(forward)
               56875125 3360.175    0.000 19894.328    0.000 optionCritic.py:91(get_action)
              697108298  657.377    0.000 19869.756    0.000 functional.py:1737(linear)
              697108298 19058.894    0.000 19058.894    0.000 {built-in method torch._C._nn.linear}
               56875125 1345.337    0.000 16075.734    0.000 optionCritic.py:80(predict_option_termination)
                2275005   46.966    0.000 8674.508    0.004 optimizer.py:84(wrapper)
              113750250 1379.746    0.000 8641.977    0.000 distribution.py:34(__init__)
                2275005   28.845    0.000 8487.754    0.004 grad_mode.py:24(decorate_context)
                2275005  126.354    0.000 8411.710    0.004 rmsprop.py:56(step)
                2275005  127.495    0.000 8141.822    0.004 _functional.py:203(rmsprop)
              530644917  542.455    0.000 7436.378    0.000 activation.py:713(forward)
               56875125  585.347    0.000 7075.422    0.000 bernoulli.py:34(__init__)
              530644917  545.326    0.000 6893.923    0.000 functional.py:1364(leaky_relu)
               56875125  560.037    0.000 6666.114    0.000 categorical.py:115(log_prob)
              530644917 6239.985    0.000 6239.985    0.000 {built-in method torch._C._nn.leaky_relu}
              172150894  392.368    0.000 5678.033    0.000 optionCritic.py:77(get_Q)
               56875125  745.899    0.000 5544.641    0.000 categorical.py:49(__init__)
                 568751   98.295    0.000 4845.113    0.009 optionCritic.py:116(critic_loss_fn)
              114319001  440.144    0.000 4640.942    0.000 optionCritic.py:88(get_terminations)
               31850064 4177.221    0.000 4177.221    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2275005   11.126    0.000 3588.533    0.002 game.py:42(step)
                2275005   19.900    0.000 3448.641    0.002 layers.py:827(step)
               56875125 2280.836    0.000 3394.586    0.000 constraints.py:398(check)
               31850064 2886.443    0.000 2886.443    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               56875125  472.705    0.000 2714.762    0.000 distribution.py:240(_validate_sample)
               56875125 2632.950    0.000 2632.950    0.000 constraints.py:364(check)
               56875125  539.348    0.000 2349.023    0.000 bernoulli.py:86(sample)
              176881639  256.380    0.000 2131.951    0.000 activation.py:101(forward)
             2736015884 2052.574    0.000 2052.740    0.000 module.py:934(__getattr__)
              398125875 1973.466    0.000 1973.466    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2275005   83.256    0.000 1895.491    0.001 layers.py:17(step)
              176881639  201.522    0.000 1875.571    0.000 functional.py:1195(relu)
               56875125  963.162    0.000 1836.283    0.000 categorical.py:123(entropy)
               56875125  145.041    0.000 1805.030    0.000 layer.py:106(move)
              171762877  282.576    0.000 1771.367    0.000 tensor.py:525(__rsub__)
               56875125 1764.210    0.000 1764.210    0.000 constraints.py:249(check)
              113750250  622.445    0.000 1719.175    0.000 functional.py:46(broadcast_tensors)
              176881639  186.599    0.000 1690.070    0.000 flatten.py:39(forward)
               56875125  389.908    0.000 1684.863    0.000 utils.py:11(broadcast_all)
              170625375  229.309    0.000 1658.828    0.000 utils.py:106(__get__)
              176881639 1644.681    0.000 1644.681    0.000 {built-in method relu}
                2275006  184.103    0.000 1525.671    0.001 layers.py:793(update)
              176881639 1503.471    0.000 1503.471    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              171762877 1457.787    0.000 1457.787    0.000 {built-in method rsub}
              114319001 1407.916    0.000 1407.916    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               25025055   58.342    0.000 1342.694    0.000 tensor.py:575(__iter__)
               56875125  372.385    0.000 1323.903    0.000 categorical.py:108(sample)
              171194126 1291.932    0.000 1291.932    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2137186465 1285.502    0.000 1285.502    0.000 {built-in method torch._C._get_tracing_state}
               56875125   66.352    0.000 1259.028    0.000 categorical.py:88(logits)
               25025055 1249.170    0.000 1249.170    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               56875125   67.768    0.000 1192.676    0.000 utils.py:82(probs_to_logits)
             9175676725 1147.340    0.000 1163.941    0.000 {built-in method builtins.len}
                 568751  938.568    0.002 1153.491    0.002 replaybuffer.py:42(sample_option_critic)
              170625375 1151.387    0.000 1151.387    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               56875125  274.461    0.000 1096.349    0.000 layers.py:844(check)
              170625375 1055.207    0.000 1055.207    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8625527279 1032.798    0.000 1032.798    0.000 {method 'values' of 'collections.OrderedDict' objects}
              113750250  920.443    0.000  920.443    0.000 {built-in method broadcast_tensors}
               56875125  837.489    0.000  837.489    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2275005   85.873    0.000  717.328    0.000 replaybuffer.py:34(save_option_critic)
               56875125  161.400    0.000  697.960    0.000 utils.py:77(clamp_probs)
              172331628  694.127    0.000  694.127    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56875125  684.486    0.000  684.486    0.000 {built-in method bernoulli}
                2275005  108.024    0.000  625.834    0.000 optimizer.py:189(zero_grad)
               56875125  584.592    0.000  584.592    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              342388252  573.241    0.000  573.241    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              753996810  324.011    0.000  541.062    0.000 {built-in method builtins.isinstance}
               56875125  536.560    0.000  536.560    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               57263142  525.427    0.000  525.427    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              113750250  495.033    0.000  495.033    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              171017966  481.531    0.000  481.531    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               56875125   85.284    0.000  473.360    0.000 layers.py:838(isFree)
               18200048  280.788    0.000  467.490    0.000 layer.py:175(NoRock_update)
               56875125  462.458    0.000  462.458    0.000 {built-in method clamp}
              176881653  444.315    0.000  444.315    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               15356287  429.024    0.000  429.024    0.000 {built-in method tensor}
               56875125  426.948    0.000  426.948    0.000 {built-in method log}
               56875125  405.776    0.000  405.776    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              268340288  335.864    0.000  388.077    0.000 layer.py:103(isFree)
              170625400  128.314    0.000  387.500    0.000 {built-in method builtins.all}
                 388041    7.628    0.000  382.792    0.001 layers.py:849(restart)
               56875125  369.318    0.000  369.318    0.000 {built-in method all}
               31850064  368.776    0.000  368.776    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               59150156  194.777    0.000  367.678    0.000 grad_mode.py:119(__enter__)
               56875125  336.813    0.000  336.813    0.000 {built-in method multinomial}
                 388041    4.698    0.000  329.683    0.001 level.py:8(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606129: <Attempt2_SuperLevel1_option_critic_1> in cluster <dcc> Done

Job <Attempt2_SuperLevel1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:11 2021
Terminated at Thu May  6 01:28:32 2021
Results reported at Thu May  6 01:28:32 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   258258.77 sec.
    Max Memory :                                 1333 MB
    Average Memory :                             1305.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15051.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258947 sec.
    Turnaround time :                            258923 sec.

The output (if any) is above this job summary.

