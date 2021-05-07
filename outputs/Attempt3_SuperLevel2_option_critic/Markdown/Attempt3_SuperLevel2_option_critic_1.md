
# Parameters

    Name :                      Attempt3_SuperLevel2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
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


      36922855151 function calls (35827882602 primitive calls) in 258900.71 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.714 258900.714 {built-in method builtins.exec}
                      1    0.334    0.334 258900.713 258900.713 <string>:1(<module>)
                      1 3872.163 3872.163 258900.379 258900.379 optionCritic.py:195(option_critic_run)
        1453209501/358339809 8910.941    0.000 107499.307    0.000 module.py:866(_call_impl)
               39344175 7677.800    0.000 106297.256    0.003 optionCritic.py:143(actor_loss_fn)
              121652188  698.510    0.000 100209.266    0.001 optionCritic.py:70(get_state)
              121652188 2262.402    0.000 97517.714    0.001 container.py:117(forward)
              243304376  861.315    0.000 65550.287    0.000 conv.py:398(forward)
              243304376  445.705    0.000 64354.797    0.000 conv.py:390(_conv_forward)
              243304376 63909.092    0.000 63909.092    0.000 {built-in method conv2d}
                1573767   10.848    0.000 59620.602    0.038 tensor.py:195(backward)
                1573767   15.207    0.000 59609.504    0.038 __init__.py:68(backward)
                1573767 59559.914    0.038 59559.914    0.038 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1573767   35.640    0.000 38177.419    0.024 optimizer.py:84(wrapper)
                1573767   21.569    0.000 38044.808    0.024 grad_mode.py:24(decorate_context)
                1573767   96.941    0.000 37985.786    0.024 rmsprop.py:56(step)
                1573767  130.282    0.000 37779.190    0.024 _functional.py:203(rmsprop)
               22032720 34249.272    0.002 34249.272    0.002 {method 'sqrt' of 'torch._C._TensorBase' objects}
               39344175 3173.232    0.000 19160.609    0.000 optionCritic.py:91(get_action)
              479991997 1471.318    0.000 17561.762    0.000 linear.py:93(forward)
              479991997  580.662    0.000 15501.640    0.000 functional.py:1737(linear)
              479991997 14802.508    0.000 14802.508    0.000 {built-in method torch._C._nn.linear}
               39344175 1064.251    0.000 11934.697    0.000 optionCritic.py:80(predict_option_termination)
               78688350 1111.324    0.000 7079.092    0.000 distribution.py:34(__init__)
              364956564  509.070    0.000 6901.054    0.000 activation.py:713(forward)
               39344175  558.770    0.000 6477.714    0.000 categorical.py:115(log_prob)
              364956564  437.709    0.000 6391.984    0.000 functional.py:1364(leaky_relu)
              364956564 5856.966    0.000 5856.966    0.000 {built-in method torch._C._nn.leaky_relu}
               39344175  717.490    0.000 5417.301    0.000 categorical.py:49(__init__)
              118497720  400.020    0.000 5209.282    0.000 optionCritic.py:77(get_Q)
                1573767    9.945    0.000 4872.232    0.003 game.py:42(step)
                1573767   16.560    0.000 4748.526    0.003 layers.py:827(step)
               39344175  330.536    0.000 4376.635    0.000 bernoulli.py:34(__init__)
               78845726  383.262    0.000 3970.433    0.000 optionCritic.py:88(get_terminations)
                1573767   71.110    0.000 3445.865    0.002 layers.py:17(step)
               39344175  224.150    0.000 3368.643    0.000 layer.py:106(move)
               39344175 2233.264    0.000 3282.889    0.000 constraints.py:398(check)
               39344175  447.365    0.000 2599.302    0.000 distribution.py:240(_validate_sample)
                 157376   29.355    0.000 2431.669    0.015 optionCritic.py:116(critic_loss_fn)
               22032720 2411.254    0.000 2411.254    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               39344175  362.946    0.000 2361.337    0.000 layers.py:844(check)
               39344175  874.993    0.000 1782.798    0.000 categorical.py:123(entropy)
              121652188  171.891    0.000 1773.534    0.000 activation.py:101(forward)
               39344175 1743.679    0.000 1743.679    0.000 constraints.py:364(check)
               39344175  319.763    0.000 1672.719    0.000 bernoulli.py:86(sample)
              118032525  210.526    0.000 1667.592    0.000 utils.py:106(__get__)
               39344175 1639.732    0.000 1639.732    0.000 constraints.py:249(check)
              121652188  142.881    0.000 1601.644    0.000 functional.py:1195(relu)
             1883625060 1579.389    0.000 1579.392    0.000 module.py:934(__getattr__)
              275409225 1461.382    0.000 1461.382    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              121652188 1433.211    0.000 1433.211    0.000 {built-in method relu}
              121652188  127.717    0.000 1402.684    0.000 flatten.py:39(forward)
              118347277  154.222    0.000 1310.492    0.000 tensor.py:525(__rsub__)
               39344175   69.667    0.000 1292.988    0.000 categorical.py:88(logits)
             1470520938 1281.675    0.000 1281.675    0.000 {built-in method torch._C._get_tracing_state}
                1573768  150.699    0.000 1279.094    0.001 layers.py:793(update)
              121652188 1274.967    0.000 1274.967    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               39344175  320.944    0.000 1257.078    0.000 categorical.py:108(sample)
               39344175   74.670    0.000 1223.321    0.000 utils.py:82(probs_to_logits)
               78688350  426.950    0.000 1215.142    0.000 functional.py:46(broadcast_tensors)
              118032525 1152.472    0.000 1152.472    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              118347277 1128.354    0.000 1128.354    0.000 {built-in method rsub}
              118189901 1080.050    0.000 1080.050    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               17311437   43.505    0.000 1024.731    0.000 tensor.py:575(__iter__)
               78845726 1016.117    0.000 1016.117    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             6442617490  975.621    0.000  988.163    0.000 {built-in method builtins.len}
               17311437  953.615    0.000  953.615    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               39344175  194.008    0.000  938.390    0.000 utils.py:11(broadcast_all)
              118032525  868.101    0.000  868.101    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5934490192  827.300    0.000  827.300    0.000 {method 'values' of 'collections.OrderedDict' objects}
               39344175  133.499    0.000  763.785    0.000 utils.py:77(clamp_probs)
               39344175  727.585    0.000  727.585    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               78688350  674.517    0.000  674.517    0.000 {built-in method broadcast_tensors}
               39344175  129.526    0.000  651.239    0.000 layers.py:838(isFree)
               39344175  630.286    0.000  630.286    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               39344175  592.053    0.000  592.053    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1573767   66.646    0.000  583.698    0.000 replaybuffer.py:34(save_option_critic)
              118504653  522.952    0.000  522.952    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
              373760136  424.304    0.000  521.712    0.000 layer.py:103(isFree)
               17311448  311.626    0.000  518.861    0.000 layer.py:159(update)
               39344175  517.122    0.000  517.122    0.000 {built-in method bernoulli}
               78688350  507.042    0.000  507.042    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               39344175  500.124    0.000  500.124    0.000 {built-in method clamp}
               39494618  492.383    0.000  492.383    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               39344175  358.441    0.000  486.090    0.000 layers.py:471(check)
                1573767   81.920    0.000  464.359    0.000 optimizer.py:189(zero_grad)
              236379802  446.639    0.000  446.639    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
             1084708377  280.796    0.000  411.347    0.000 enum.py:646(__hash__)
               22032720  399.450    0.000  399.450    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               39344175  384.865    0.000  384.865    0.000 {built-in method log}
               39344175  377.041    0.000  377.041    0.000 {built-in method all}
               39344175  261.507    0.000  353.658    0.000 layers.py:77(check)
               39344175  212.493    0.000  346.173    0.000 layers.py:246(check)
               39344175  343.412    0.000  343.412    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              118032550   95.066    0.000  342.829    0.000 {built-in method builtins.all}
                9914734  328.049    0.000  328.049    0.000 {built-in method tensor}
                 157376  257.035    0.002  327.560    0.002 replaybuffer.py:42(sample_option_critic)
               39193733   66.078    0.000  311.593    0.000 {built-in method builtins.any}
              518106028  203.958    0.000  307.262    0.000 {built-in method builtins.isinstance}
               22032720  303.310    0.000  303.310    0.000 {method 'add_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607859: <Attempt3_SuperLevel2_option_critic_1> in cluster <dcc> Done

Job <Attempt3_SuperLevel2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:25 2021
Job was executed on host(s) <n-62-21-101>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:27 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

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

    CPU time :                                   258905.23 sec.
    Max Memory :                                 1176 MB
    Average Memory :                             1159.49 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15208.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259010 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

